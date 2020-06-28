# Modularity

## Bed probes

![](assets/images/probes.png)

EVA platform follows a simple standard for different bed probe mounts. Each carriage has 2 vertically alligned M3 screw holes, 8mm apart.
All probe mounts follow this standard but there are special veriants of probes where a probe mount had to be modified to fit a carriage (i.e. BL-Touch on the Aero Assembly).

| Probe Type           | File                 | Link                                                                                         |
| -------------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| 8mm inductive probe  | lj8_probe_right.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/lj8_probe_right.stl)  |
| 8mm inductive probe  | lj8_probe_left.stl   | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/lj8_probe_left.stl)   |
| 8mm inductive probe  | lj8_probe_center.stl | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/lj8_probe_center.stl) |
| 12mm inductive probe | lj12_probe_right.stl | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/lj12_probe_right.stl) |
| 12mm inductive probe | lj12_probe_left.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/lj12_probe_left.stl)  |
| BL-Touch             | bl_touch.stl         | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/bl_touch.stl)         |
| BL-Touch             | bl_touch_thick.stl   | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/Probe%20Mounts/bl_touch_thick.stl)   |

## MGN12 and MGN15

All listed assemblies are pointing to MGN15 variants but a smaller (and probably better) MGN12 vartiant is now also available. MGN12 is lighter so it's a good choice for a CoreXY system to make the X rail assembly lighter. Both variants are fully compatible with each other, which means that you only need to change the MGN rail, your top and bottom parts and you are set.

![](assets/images/MGN12_15.png)

## Back Fan duct angles

There are 5 different variants available. From the least Y space consuming 90deg variant down to 30deg that can potentially fit under the frame while providing a straight air path to the duct.

![](assets/images/back_angles.png)

## Layer Cooling

Since version 1.2.0 EVA has support for Volcano hot ends. Check out the results of a [CFD simulation](/cfd). All available air ducts are listed below, notice the ones called `risen` - those have a higier tolerance if you'll run into issues with the standard ones (the tips are moved 1mm more from the bed):

![](assets/images/fan_ducts.png)

| Air duct           | File                 | Link                                                                                         |
| -------------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| Straight | horn_duct_v2_straight.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_straight.stl)  |
| Straight risen | horn_duct_v2_straight_risen.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_straight_risen.stl)  |
| Angled | horn_duct_v2_angled_20deg.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_angled_20deg.stl)  |
| Angled risen | horn_duct_v2_angled_20deg_risen.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_angled_20deg_risen.stl)  |
| Straight Volcano | horn_duct_v2_volcano_straight.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_volcano_straight.stl)  |
| Straight Volcano risen  | horn_duct_v2_volcano_straight_risen.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_volcano_straight_risen.stl)  |
| Angled Volcano | horn_duct_v2_volcano_angled_20deg.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_volcano_angled_20deg.stl)  |
| Angled Volcano risen | horn_duct_v2_volcano_angled_20deg_risen.stl  | [GitHub](https://github.com/pkucmus/EVA/blob/master/stl/horn_duct_v2_volcano_angled_20deg_risen.stl)  |

## Tension Sliders

If you have a 6mm belt based printer or the orientation of the teeth on your belts are diffreent then look for different sliders - there's quite a few provided:

![](assets/images/sliders.png)
