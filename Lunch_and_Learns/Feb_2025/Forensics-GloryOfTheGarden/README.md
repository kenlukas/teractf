# Glory of the Garden

## Forensics

### This garden contains more than it seems.

First download the file linked in the challenge

When I get an image file, the first thing I do is check if it's truly an image file.

```sh
$ file garden.jpg 
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3
```
Yes, it's an image file.  Next, I'd look at the metadata using `exiftool`.

```sh
$ exiftool garden.jpg 
ExifTool Version Number         : 12.40
File Name                       : garden.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2020:10:26 18:39:31+00:00
File Access Date/Time           : 2025:01:29 14:25:48+00:00
File Inode Change Date/Time     : 2025:01:29 14:25:36+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
[ Lots of uninteresting output deleted ]
Megapixels                      : 6.7
```
Nothing of interest in the metadata. My next step would be to view the image in a browser, or a tool like Gimp or Image Magick to check for something obvious.

![garden.jpg](./garden.jpg)

Before diving down a rabbit hole, I'd check if there are any interesting strings.

```sh
$ strings garden.jpg |grep pico
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```
And there it is.  Full disclosure, you don't need the `grep` command because the flag is the last line output.

**picoCTF{more_than_m33ts_the_3y3657BaB2C}**
