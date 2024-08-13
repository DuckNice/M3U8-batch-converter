## Steps:

1. Setup file list (See **_File list structure_** for details)

2. run the _pilfer_ notebook to download the m3u8 from the file list

3. Run the _convert_m3u8_ function in the _download_ notebook to convert the m3u8 to local hvec or av1 files.

## File list structure

The file list format points to all the source files to be downloaded and describes their folder hierarchy

> All empty lines are ignored.

- Start a line with '-' to enter a folder: - { _Folder name_ }
  > A folder is created if not already present
- Write a line with _'--'_ to step out of a folder
- A video entry is of the format <br/>
  { _Video link_ } - { _Video name_ }
  > The Files pointed to MUST be of the type _m3u8_

### Example

<p>
- Root folder name<br/>
https.//example.com/file.m3u8?get=parameters_are_allowed - intro video<br/>

\- Nested folder<br/>
https.//example.com/file.m3u8 - file name 1<br/>
https.//example.com/file.m3u8 - file name 2<br/>

--<br/>
\- Other folder<br/>
https.//example.com/file.m3u8 - same names will not conflict<br/>
https.//example.com/file.m3u8 - same names will not conflict<br/>

-- <br/>
\- Other folder<br/>
https.//example.com/file.m3u8 - new file in same folder<br/>

</p>
