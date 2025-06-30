# Slint Compilation Fix

## Problem

The original settings app had Slint compilation errors due to syntax issues:

```
Error running the application: ('Could not compile C:\\Users\\adam0\\slint-python-template\\src\\settings_app\\ui\\SettingsWindow.slint', [<builtins.PyDiagnostic object at 0x000002A3F01E64C0>])
```

## Root Cause

The main issues were:

1. **Hyphenated property names**: Slint doesn't handle property names with hyphens (`-`) well
2. **Inconsistent callback naming**: Mixed hyphen and underscore usage
3. **Property binding syntax**: Some property bindings weren't properly formatted

## Fixes Applied

### 1. Property Names (Hyphens → Underscores)

**Before:**
```slint
in-out property <float> detection-threshold-x: 3;
in-out property <float> upper-color-r: 154;
callback detection-threshold-x-changed(float);
```

**After:**
```slint
in-out property <float> detection_threshold_x: 3;
in-out property <float> upper_color_r: 154;
callback detection_threshold_x_changed(float);
```

### 2. Callback Names (Consistent Underscores)

**Before:**
```slint
callback value-changed(float);
value-changed(val) => {
    root.detection-threshold-x-changed(val);
}
```

**After:**
```slint
callback value_changed(float);
value_changed(val) => {
    root.detection_threshold_x_changed(val);
}
```

### 3. Property Bindings

**Before:**
```slint
current-value <=> root.current-value;
```

**After:**
```slint
current-value <=> root.current_value;
```

## Files Updated

1. **SettingsWindow.slint** - Main window with all property and callback names
2. **DetectionSettings.slint** - Detection settings view
3. **AimSettings.slint** - Aim settings view  
4. **SliderGroup.slint** - Slider component
5. **ComboBoxGroup.slint** - Combo box component

## Testing

Created `test_slint_compilation.py` to verify all Slint files compile correctly:

```bash
python3 test_slint_compilation.py
```

This tests:
- Simple test window
- Individual components
- View components  
- Main settings window

## Result

All Slint files now compile successfully with proper syntax. The app should run without compilation errors.

## Running the App

After the fixes, you can run the settings app with:

```bash
python3 run_settings_app.py
```

Or test compilation first:

```bash
python3 test_slint_compilation.py
```