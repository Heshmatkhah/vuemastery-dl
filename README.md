# vuemastery-dl
[VueMastery](https://www.vuemastery.com/courses) video downloader

You can see [List of existing courses in here](CoursesList.md)

## Download an entire course:
### Using nodejs script
* first `cd data/ANY_DIRRECTORY` like `cd data/advanced-components`
* download a directory with `node ../../mirror.js`

## Download all courses

If you want to download all courses, you can use the `downloadAll.sh` script. 

```bash
# give execution rights to the script
chmod +x ./downloadAll.sh

# run using node
./downloadAll.sh

# run using python
./downloadAll.sh --python
```

### Using python script
The script required **Python 3.6+** and **requests** package.
you can install it with `pip install requests`

1. first `cd` to the direcoty of the course you want: `cd data/ANY_DIRRECTORY` like `cd data/advanced-components`
2. download entire course with `python3 ../../course-downloader.py`

you can use this options:
* `-q` for setting video quality: `-q 1080`
    if the given quality was unavailable, the highest available quality will be used  
* `-s` for downloading subtitles: `-s`
* `-l` for subtitles language: `-l en`

as rate limit policy applied to subtitle files, downloading a subtitle may fail. in this situation,
the subtitle file will contain the subtitle like.  

## Finding video links (for contributors)
* Open a lesson on the browser
* Run `document.getElementsByTagName('iframe')[0].src` in the browser's console to get {Video LINK}
* Run `node download.js {Video LINK}` in project directory. Also you can set quality of video `node download.js {Video LINK} 720`, Default set to 1080
* Run `node sitemap.js` to get list of courses

# PR
Please put new video links to the data folder to help others, If you still have access to the videos.

## Videos not yet completely added:

* [**Touring Vue Router**](https://www.vuemastery.com/courses/touring-vue-router/)
   1. [2021-04-27] Lesson 10: Global and Per-Route Guards
   2. [2021-05-18] Lesson 11: Lazy Loading Routes
* [**Real World Testing**](https://www.vuemastery.com/courses/real-world-testing/)
   1. [2021-05-04] Lesson 2: Setup & Testing like a User
   2. [2021-05-11] Lesson 3: Mocking Vuex Stores
* [**Vuex Fundamentals**](https://www.vuemastery.com/courses/vuex-fundamentals/)
   1. [2021-05-04] Lesson 3: Updating State
   2. [2021-05-25] Lesson 4: Fetching State
   3. [2021-06-01] Lesson 5: Error Handling
   4. [2021-06-08] Lesson 6: Next Steps