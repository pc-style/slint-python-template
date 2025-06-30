# Settings Configuration App

A comprehensive GUI application for configuring detection and aim settings, built with Slint and Python.

## Features

### Detection Settings
- **Detection Threshold**: Configure X and Y threshold values (0-10)
- **Color Settings**: RGB values for upper and lower color bounds (0-255)
- **Contour & Clustering**: 
  - Min contour area (0-1000 px²)
  - Density threshold (0-1)
  - Enable/disable clustering
  - Cluster distance (0-100 px)
  - Min/max cluster sizes (0-50000 px²)
- **Field of View**: FOV X/Y and Aim FOV X/Y settings (100-1000 px)
- **Display Settings**: 
  - FPS control (30-240 fps)
  - Auto-detect resolution toggle
  - Manual resolution settings (800x600 to 3840x2160)

### Aim Settings
- **Basic Aim Settings**:
  - Aim offset (-50 to 50 px)
  - Smoothing (0.1-1.0)
  - Base speed (0.1-2.0)
  - Y speed (0.1-1.0)
  - Aim height (0.1-1.0)

- **Smoothing Settings**:
  - Smoothing type (linear, ease_in_out, bezier)
  - Ease factor (1.0-5.0)
  - Min ease speed (0.0-1.0)
  - Bézier control offset (0.0-1.0)
  - Bézier tension (0.1-2.0)

- **Movement Settings**:
  - Movement randomness (0.0-0.5)
  - Deadzone (0-50 px)

- **Anti-Shake Settings**:
  - Enable/disable anti-shake
  - Anti-shake threshold (0.01-0.2)
  - Shake suppression factor (0.1-1.0)
  - Shake escalation threshold (0.1-0.5)
  - Shake escalation rate (0.05-0.3)
  - Shake cooldown duration (0.5-10.0 sec)

## Default Values

The app initializes with the following default values:

```
detection_threshold = 3, 3
upper_color = 154, 165, 175
lower_color = 141, 88, 58
min_contour_area = 261
density_threshold = 0.5
enable_clustering = true
cluster_distance = 40
min_cluster_size = 1000
max_cluster_size = 20000
fov_x = 400
fov_y = 400
aim_fov_x = 400
aim_fov_y = 400
fps = 120
auto_detect_resolution = true
resolution_x = 1920
resolution_y = 1080

[aim]
offset = 0
smooth = 0.9
speed = 0.5
y_speed = 0.2
aim_height = 0.7
smoothing_type = bezier
ease_factor = 2.0
min_ease_speed = 0.2
bezier_control_offset = 0.3
bezier_tension = 1.0
movement_randomness = 0.1
deadzone = 10
enable_anti_shake = true
anti_shake_threshold = 0.05
shake_suppression_factor = 0.7
shake_escalation_threshold = 0.2
shake_escalation_rate = 0.1
shake_cooldown_duration = 2.0
```

## Usage

### Running the App

1. **Using the run script**:
   ```bash
   python run_settings_app.py
   ```

2. **Using the module directly**:
   ```bash
   python -m src.settings_app
   ```

### Interface

The app features a modern, tabbed interface with two main sections:

1. **Detection Settings Tab**: All detection-related configuration options
2. **Aim Settings Tab**: All aim-related configuration options

### Controls

- **Sliders**: Drag to adjust numeric values, or click to set precise values
- **Checkboxes**: Toggle boolean options on/off
- **Combo Boxes**: Select from predefined options (e.g., smoothing type)
- **Save Settings**: Export current configuration to `settings.json`
- **Load Settings**: Import configuration from `settings.json`
- **Reset to Defaults**: Restore all settings to their default values

### Settings File

The app saves/loads settings in JSON format. Example structure:

```json
{
  "detection_threshold": [3, 3],
  "upper_color": [154, 165, 175],
  "lower_color": [141, 88, 58],
  "min_contour_area": 261,
  "density_threshold": 0.5,
  "enable_clustering": true,
  "cluster_distance": 40,
  "min_cluster_size": 1000,
  "max_cluster_size": 20000,
  "fov_x": 400,
  "fov_y": 400,
  "aim_fov_x": 400,
  "aim_fov_y": 400,
  "fps": 120,
  "auto_detect_resolution": true,
  "resolution_x": 1920,
  "resolution_y": 1080,
  "aim": {
    "offset": 0,
    "smooth": 0.9,
    "speed": 0.5,
    "y_speed": 0.2,
    "aim_height": 0.7,
    "smoothing_type": "bezier",
    "ease_factor": 2.0,
    "min_ease_speed": 0.2,
    "bezier_control_offset": 0.3,
    "bezier_tension": 1.0,
    "movement_randomness": 0.1,
    "deadzone": 10,
    "enable_anti_shake": true,
    "anti_shake_threshold": 0.05,
    "shake_suppression_factor": 0.7,
    "shake_escalation_threshold": 0.2,
    "shake_escalation_rate": 0.1,
    "shake_cooldown_duration": 2.0
  }
}
```

## Dependencies

- Python 3.7+
- slint-ui
- screeninfo
- json (built-in)

## File Structure

```
src/settings_app/
├── __init__.py
├── __main__.py
├── app.py                          # Main application logic
└── ui/
    ├── SettingsWindow.slint        # Main window
    ├── components/
    │   ├── SliderGroup.slint       # Reusable slider component
    │   ├── CheckboxGroup.slint     # Reusable checkbox component
    │   └── ComboBoxGroup.slint     # Reusable combo box component
    └── views/
        ├── DetectionSettings.slint # Detection settings tab
        └── AimSettings.slint       # Aim settings tab
```

## Customization

The app is highly modular and can be easily extended:

1. **Add new settings**: Update the `SettingsConfig` class and add corresponding UI controls
2. **Modify UI**: Edit the `.slint` files to change the interface
3. **Change defaults**: Update the default values in `SettingsConfig.__init__()`
4. **Add validation**: Implement value validation in the callback methods

## License

This project follows the same license as the parent template project.