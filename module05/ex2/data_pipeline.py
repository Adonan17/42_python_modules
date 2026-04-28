#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        value: str = self._data.pop(0)
        rank: int = self._rank
        self._rank += 1
        return (rank, value)

    @property
    def remaining(self) -> int:
        return len(self._data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            return all(type(x) in (int, float) for x in data)
        return False

    def ingest(  # type: ignore[override]
        self, data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: list[int | float] = (
            data if isinstance(data, list) else [data]
        )
        for x in items:
            self._data.append(str(x))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        if isinstance(data, list):
            return all(type(x) is str for x in data)
        return False

    def ingest(  # type: ignore[override]
        self, data: str | list[str]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: list[str] = data if isinstance(data, list) else [data]
        for x in items:
            self._data.append(x)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def _ok(e: Any) -> bool:
            return (
                type(e) is dict
                and "log_level" in e and "log_message" in e
                and type(e["log_level"]) is str
                and type(e["log_message"]) is str
            )
        if type(data) is dict:
            return _ok(data)
        if isinstance(data, list):
            return all(_ok(x) for x in data)
        return False

    def ingest(  # type: ignore[override]
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for x in items:
            self._data.append(f"{x['log_level']}: {x['log_message']}")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        row = ",".join(value for _rank, value in data)
        print("CSV Output:")
        print(row)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._totals: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._totals[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    if isinstance(element, list):
                        count: int = len(element)
                    else:
                        count = 1
                    self._totals[proc] += count
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't process"
                    f" element in stream: {element}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining > 0:
                    batch.append(proc.output())
            if batch:
                plugin.process_output(batch)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            total = self._totals[proc]
            remaining = proc.remaining
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    pipeline = DataStream()

    print("Initialize Data Stream...")
    pipeline.print_processors_stats()
    print()

    print("Registering Processors")
    pipeline.register_processor(NumericProcessor())
    pipeline.register_processor(TextProcessor())
    pipeline.register_processor(LogProcessor())

    batch1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch1}")
    pipeline.process_stream(batch1)
    pipeline.print_processors_stats()
    print()

    csv_plugin = CSVExportPlugin()
    print("Send 3 processed data from each processor to a CSV plugin:")
    pipeline.output_pipeline(3, csv_plugin)
    pipeline.print_processors_stats()
    print()

    batch2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {batch2}")
    pipeline.process_stream(batch2)
    pipeline.print_processors_stats()
    print()

    json_plugin = JSONExportPlugin()
    print("Send 5 processed data from each processor to a JSON plugin:")
    pipeline.output_pipeline(5, json_plugin)
    pipeline.print_processors_stats()


if __name__ == "__main__":
    main()
