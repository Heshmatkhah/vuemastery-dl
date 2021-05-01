import argparse
import os
from importlib import import_module

get_video_info = import_module('course-downloader').get_video_info
rootdir = "./data"

parser = argparse.ArgumentParser(description='Vue Mastery Course Readme Generator')
parser.add_argument('-n', '--no-name', action='store_false', help="Don't get lesson name")

if __name__ == "__main__":
	args = parser.parse_args()

	with open(os.path.join('./CoursesList.md'), 'w') as courses_list:
		for dir_name in os.listdir(rootdir):
			if os.path.isdir(os.path.join(rootdir, dir_name)):
				course_name = dir_name.title().replace('-', ' ')
				print(course_name)
				courses_list.write(f"# {course_name}\n")
				courses_list.write(f"* [View on VueMastery.com](https://vuemastery.com/courses/{dir_name})\n")
				courses_list.write(f"* [Readme]({rootdir}/{dir_name}/Readme.md)\n\n")

				with open(os.path.join(rootdir, dir_name, 'data.txt'), 'r') as link_file, open(os.path.join(rootdir, dir_name, 'Readme.md'), 'w') as readme_file:
					readme_file.write(f"# {course_name}\n")
					readme_file.write(f"[View on VueMastery.com](https://vuemastery.com/courses/{dir_name})\n\n")
					readme_file.write(f"**You should check each lesson contents in the associated readme files**\n\n")
					for num, line in enumerate(link_file, start=1):
						if args.no_name:
							video_inf = get_video_info(line)
							readme_file.write(f"{num}. [Lesson {num:02}: **{video_inf['title']}**]({line.strip()})\n")
						else:
							readme_file.write(f"{num}. [Lesson {num:02}]({line.strip()})\n")
