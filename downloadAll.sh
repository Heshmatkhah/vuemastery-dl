#! /bin/bash

PYTHON=false
ZIP=false
REMOVE=false

# fetch the variables
while [ "$1" != "" ]; do
	case $1 in
	--python)
		PYTHON=true
		;;
	--zip)
		ZIP=true
		;;
	--zip-and-remove)
		ZIP=true
		REMOVE=true
		;;
	*)
		echo "Invalid parameter"
		exit 1
		;;
	esac
	shift
done

DIRECTORIES=$(find data -type d -name "*")
BASE=$(pwd)

first=true
for directory in $DIRECTORIES; do
	# do not include parent directory
	if [[ "$first" == true ]]; then
		first=false
		continue
	fi

	fullPath="$BASE/$directory"
	name="$(basename -- "$directory")"

	echo "Downloading courses for: $name"

	cd "$fullPath"

	if [[ "$PYTHON" == true ]]; then
		python3 ../../course-downloader.py
	else
		node ../../mirror.js
	fi

	echo -e "Download course $name done!\n"

	if [[ "$ZIP" == true ]]; then
		echo -e "Zipping $name:"
		cd ..
		zip -r "$name" $name
		echo "$name Zipped!" $name
	fi

	if [[ "$REMOVE" == true ]]; then
		cd "$fullPath"
		cd ..
		rm -rf $name
		echo "$name deleted!" $name
	fi

	echo "$name ...Done!"
done

echo "Done!"
