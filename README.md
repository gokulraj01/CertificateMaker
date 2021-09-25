# Certificate Generator

A Python Based basic Certificate Generation Utility for bulk generation.

## Changelog

### v. 3.0
- Added GUI Positioning tool for finding x, y offsets in images in one step instead of trial and error.
- Support for local .ttf Font Faces.

- Reports can now be made in CSV and JSON formats using `CertGen.makeCSVReport()` and `CertGen.makeJSONReport()` after certificate generation.
- Improved Human Friendly layout for reports
- n-data fields supports in reports (from previous 2 limit). Data can be passed along via `CertGen.makeCertificate()`
    ```py
    Certgen.makeCertificate(
        title: str,
        filename: str,
        uid: list   # list of data fields to use in report
        )
    ```
- Minor bug fixes and improvements

<hr>

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

<hr>

### v. 1.0
- Support for single centered string parameter with variable y-axis positioning
    - Intended Use --> Names
- Dynamic File Naming
- Support for dynamic PDF titles
