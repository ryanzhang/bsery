#!/usr/bin/env bash
while getopts a:n:u:d: flag
do
    case "${flag}" in
        a) author=${OPTARG};;
        n) name=${OPTARG};;
        u) urlname=${OPTARG};;
        d) description=${OPTARG};;
    esac
done

echo "Author: $author";
echo "Project Name: $name";
echo "Project URL name: $urlname";
echo "Description: $description";

echo "Renaming project..."

original_author="ryanzhang"
original_name="bsery"
original_urlname="bsery"
original_description="Awesome bsery created by ryanzhang"
# for filename in $(find . -name "*.*") 
for filename in $(git ls-files) 
do
    sed -i "s/$original_author/$author/g" $filename
    sed -i "s/$original_name/$name/g" $filename
    sed -i "s/$original_urlname/$urlname/g" $filename
    sed -i "s/$original_description/$description/g" $filename
    echo "Renamed $filename"
done

mv bsery $name
find . -name "*bsery*" |  sed  's/\(\(.*\)bsery\(.*\)\)/\1 \2bsery\3/g' | while read name1 name2; do mv $name1 $name2; done

# This command runs only once on GHA!
rm -rf .github/template.yml
