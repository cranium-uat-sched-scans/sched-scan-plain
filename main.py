import json
from datetime import datetime, timezone


def report() -> str:
    return json.dumps({"generated_at": datetime.now(timezone.utc).isoformat()})


if __name__ == "__main__":
    print(report())
