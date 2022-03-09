# File Type Finder

File type finder lists paths and file names for files with certain extensions in a repository. The action allows you to input a path to search in or a `csv` file. The action is useful when you are trying to find all your files of a certain type or if you want to input files of a certain type to another action.

# Usage

See [main.yml](.github/workflows/main.yml).

```yaml
- name: File type finder action
    id: ftf
    uses: ab185508/file-type-finder@main
    with:
        path: "/"
        type: ".yml"
```

# Inputs
```path```: (Optional) Path to where you want to the search to run. Set to `"/"` if you want to search the whole repo.

```type```: (Required) The type of file you want to search for.

```fileinput```: (Optional) Boolean to indicate if you want to provide a file input. This is set to `false` by default.

```file```: (Optional) Path or reference to the file you are passing in. See [testcase1](.github/workflows/testcase1.yml) to see how this can be applied with a reference to an output from another action.

```extchange```: (Optional) Boolean to indicate if you want to output to an additional list that has all the file extensions changed to something new. This is added as it provides a useful tool when working with file conversion actions. The value is set to `false` by default.

```ext```: (Optional) The extension you want to convert to. See [testcase2](.github/workflows/testcase2.yml) for a reference on this.

# Outputs
```paths```: A list of the paths to the files that contain the desired extension.

```names```: All the names of the files that contain those desired extensions.

```extaddpaths```: A list of the paths to the files with the desired extension but the extension is converted to the one provided in the `ext` input.

# Example Workflows

## Case 1 [testcase1](.github/workflows/testcase1.yml) 

Gets modified files using another action and takes in the CSV from that as input. Then it runs through the files and finds the ones that end in `.yml`.

```yaml
- name: File type finder action
    id: ftf
    uses: ab185508/file-type-finder@main
    with:
        path: "/"
        type: ".yml"
        fileinput: true
        file: ${{ steps.files.outputs.added_modified }}
```

## Case 2 [testcase2](.github/workflows/testcase2.yml) 

Gets modified files using another action and takes in the CSV from that as input. Then it runs through the files to find the ones that end in `.drawio`, afterwhich it takes the extension for all those files and swaps it to `.png`.

```yaml
- name: File type finder action
    id: ftf
    uses: ab185508/file-type-finder@main
    with:
        type: ".drawio"
        fileinput: true
        file: ${{ steps.files.outputs.added_modified }}
        extchange: true
        ext: '.png'
```