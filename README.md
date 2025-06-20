# osuSkinRemoveSD

removes non-HD elements from an osu! skin

elements that don't have an HD version won't be removed

if you have a skin folder that's laid out like so:
```
skinname/
  cursor.png
  cursor@2x.png
  cursortrail.png
  hitcircle.png
  hitcircleoverlay.png
  hitcircleoverlay@2x.png
```
then after running the script you'll be left with:
```
skinname/
  cursor@2x.png
  cursortrail.png
  hitcircle.png
  hitcircleoverlay@2x.png
```
