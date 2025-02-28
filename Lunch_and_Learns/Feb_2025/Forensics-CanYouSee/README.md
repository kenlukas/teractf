# CanYouSee

## Forensics

### How about some hide and seek?

Use the `wget` command to download the file.

First unzip the file.  It will output a file: ukn_reality.jpg

Check if it's truly a JPEG file.

```sh
$ file ukn_reality.jpg 
ukn_reality.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 4308x2875, components 3
```

Yep, if you open the file in a browser you'll see there's not much to go on.

![ukn_reality.jpg](./ukn_reality.jpg)

For image forensics, `exiftool` is a staple for viewing metadata.

```sh
$ exiftool ukn_reality.jpg 
ExifTool Version Number         : 12.40
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2024:02:15 22:40:17+00:00
File Access Date/Time           : 2025:01:28 14:49:13+00:00
File Inode Change Date/Time     : 2025:01:28 14:49:06+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

What catches my eye immediately is the value of Attribution URL.  This looks like a Base64 hash.  Normally, I'd just cut and paste this into `CyberChef` and run the `From Base64` recipe and see the output, BUT!!! we want to use pipes for this.

First, look at the `man` page for `exiftool`.  If you look at the examples you'll find one describing printing the meta information. The format will use the -T (print in tabular format), and the meta data field without spaces -AttributionURL

```sh
$ exiftool -T -AttributionURL ukn_reality.jpg 
cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==
```

Another command in Unix is `base64`.  This command can convert data to base64 or decode base64.  Check out the man page.  We'll use the -d to decode

```sh
$ exiftool -T -AttributionURL ukn_reality.jpg |base64 -d 
picoCTF{ME74D47A_HIDD3N_4dabddcb}
```

Cool, found the flag.  To reinforce there's multiple ways to solve a problem in Unix, let's use `grep` and some new commands.  The first is `cut`.  The man page tells you it prints selected parts of lines.  You select a delimiter, a character(including a space) to cut the line into pieces on.  You also need to tell it the number of bytes, characters or fields.  We'll use fields.

If you recall, the exiftool output for the Attribution field was `Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==`

We want everything to the right of the `:` so lets use that as the delimiter and select the second field (you may wonder why this tool doesn't start counting at 0, ¯\\\_(ツ)\_/¯).

```sh
$ exiftool ukn_reality.jpg| grep Attribu | cut -f 2 -d ":"
 cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==
```
Now if we pipe that output into base64 will give an error because of that pesky space at the beginning, so well need another tool named `tr` which is short for translate.  We'll use the -d option to delete the space.

```sh
$ exiftool -S ukn_reality.jpg| grep Attribu | cut -f 2 -d ":" |tr -d ' '           
cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==
```
Better...and if we pipe that output into `base64` we get the flag (again)

```sh
$ exiftool -S ukn_reality.jpg| grep Attribu | cut -f 2 -d ":" |tr -d ' ' |base64 -d
picoCTF{ME74D47A_HIDD3N_4dabddcb}
```

NOTE:  To avoid needing to use the `tr` command, notice there's a space after the colon, if you use that as the delimiter you get the base64 string without the space.


**picoCTF{ME74D47A_HIDD3N_4dabddcb}**
