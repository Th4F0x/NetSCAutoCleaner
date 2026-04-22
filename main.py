import json
import shutil
from pathlib import Path

def main():
    configpath = Path("config.json")
    if not configpath.exists():
        print("Конфиг не найден")
        return
    
    try:
        with open(configpath, "r", encoding="utf-8") as f:
            target = json.load(f).get("targets", {})
    except json.JSONDecodeError:
        print("Ошибка Json")
        return
    
    for label, path_str in target.items():
        path = Path(path_str)
        if not path.is_dir():
            print(f"{label}: путь не найден ({path_str})")
            continue
    
        print(f"🧹 {label}")

        for item in list(path.iterdir()):
            try:
                if item.is_file():
                    item.unlink(missing_ok=True)
                elif item.is_dir():
                    shutil.rmtree(item, ignore_errors=True)
            except Exception as e:
                print(f"Пропущено: {item} ({e})")
    
    print("Clean Done")

if __name__ == "__main__":
    main()