# Certificate Generator

A Python Based basic Certificate Generation Utility for bulk generation.

## Changelog
### v. 2.1
- Minor bug fixes and improvements
- Removed reduntant image scaling

### v. 2.0
- Arbitrary fields support added through new function `drawCenString()` with individual customization provision
    ```py
    CertGen.drawCenString(
        data: str,      # the string to display
        size: int,      # font size in pt
        x_offset: int,  # offset in pt from page center
        y: int,         # position from bottom of page
        font_name: str  # name of fontFace source file (TrueType)
        )
    ```
- Auto Centificate Serial Numbering via `initSerial()` with user specified prefix

### v. 1.0
- Support for single centered string parameter with variable y-axis positioning
    - Intended Use --> Names
- Dynamic File Naming
- Support for dynamic PDF titles
