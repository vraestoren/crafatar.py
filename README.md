# <img src="https://avatars.githubusercontent.com/u/10799315?s=200&v=4" width="28" style="vertical-align:middle;" /> crafatar.py

> API wrapper for [Crafatar](https://crafatar.com) — fetch and save Minecraft player avatars, skins, capes, and renders based on UUID.

## Quick Start
```python
from crafatar import Crafatar

crafatar = Crafatar(player_uuid="069a79f4-44e9-4726-a5be-fca90e38aaf5")

# Save player avatar to current directory
crafatar.get_player_avatar()
```

---

## Constructor Options
```python
Crafatar(
    player_uuid="069a79f4-44e9-4726-a5be-fca90e38aaf5"  # Minecraft player UUID
)
```

---

## Methods

| Method | Description |
|--------|-------------|
| `get_player_avatar(size)` | Download and save the player's face avatar |
| `get_player_head()`| Download and save the player's 3D head render |
| `get_player_body()` | Download and save the player's full body render |
| `get_player_skin()` | Download and save the player's raw skin texture |
| `get_player_cape()` | Download and save the player's cape texture |

All methods return `True` on success and save a `.png` file to the specified location.

---

## Saving to a Custom Location

All methods internally call `_save(content, location)`. To save to a custom path, modify the `location` argument:
```python
crafatar = Crafatar(player_uuid="069a79f4-44e9-4726-a5be-fca90e38aaf5")

# Files are saved as {random_id}-{player_uuid}.png
crafatar.get_player_avatar(size=256)
```

> Files are saved as `{random_id}-{player_uuid}.png` in the current working directory by default.
