import json
from phoebe_core import PhoebeCore
from gui import PhoebeGUI


def main() -> None:
    core = PhoebeCore()
    with open("identity/identity.json", "r", encoding="utf-8") as f:
        identity = json.load(f)
    core.brain.update_identity(identity.get("name", "Phoebe"))
    reflection = core.cycle()
    print(reflection)
    gui = PhoebeGUI()
    gui.display_message("Phoebe", reflection)
    gui.run()


if __name__ == "__main__":
    main()
