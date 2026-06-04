import io

path = "/Users/sencha/vegaWorkshop/VegaWorkshopApp/src/screens/HomeScreen.tsx"

with io.open(path, "r", encoding="utf-8") as f:
    src = f.read()

# 1) Add a focusCount state right after backgroundImage state.
anchor_state = "  const [backgroundImage, setBackgroundImage] = useState<string>('');\n"
assert anchor_state in src, "state anchor not found"
src = src.replace(
    anchor_state,
    anchor_state
    + "\n"
    + "  // BUG: tracking the focus count at the screen level forces the ENTIRE\n"
    + "  // HomeScreen (every ContentRow and ThumbnailItem) to re-render on every\n"
    + "  // D-pad focus change, even though the rows and thumbnails have not changed.\n"
    + "  const [focusCount, setFocusCount] = useState(0);\n",
    1,
)

# 2) Increment focusCount inside handleItemFocus.
anchor_focus = (
    "  const handleItemFocus = (item: MovieItem) => {\n"
    "    // setBackgroundImage(item.images.poster_16x9);\n"
    "    setBackgroundImage(item.images.thumbnail_450x253);    \n"
    "  };\n"
)
assert anchor_focus in src, "handleItemFocus anchor not found"
src = src.replace(
    anchor_focus,
    "  const handleItemFocus = (item: MovieItem) => {\n"
    "    setBackgroundImage(item.images.thumbnail_450x253);\n"
    "    // BUG: bumps screen-level state on every focus -> full-tree re-render.\n"
    "    setFocusCount((c) => c + 1);\n"
    "  };\n",
    1,
)

# 3) Render focusCount so it is actually used (and visible on screen).
anchor_overlay = "      {/* Dark Overlay */}\n      <View style={styles.overlay} />\n"
assert anchor_overlay in src, "overlay anchor not found"
src = src.replace(
    anchor_overlay,
    "      {/* Dark Overlay */}\n"
    "      <View style={styles.overlay} />\n"
    "\n"
    "      {/* BUG: focus counter re-renders the whole screen on every focus move */}\n"
    "      <Text style={styles.focusCounter}>Focus changes: {focusCount}</Text>\n",
    1,
)

# 4) Add a style for focusCounter.
anchor_style = "  rowContainer: {\n"
assert anchor_style in src, "style anchor not found"
src = src.replace(
    anchor_style,
    "  focusCounter: {\n"
    "    position: 'absolute',\n"
    "    top: 20,\n"
    "    right: 40,\n"
    "    color: '#FFFFFF',\n"
    "    fontSize: 24,\n"
    "  },\n"
    "  rowContainer: {\n",
    1,
)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(src)

print("Re-render bug injected.")
