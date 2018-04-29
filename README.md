# Image RGB Ratio
Project in Linear Algebra course which converts an image to RGB Matrix using Numpy, PIL and scipy Libs and uses manim animation engine to show how RGB ratio is changing

# manim
[Original repo] (https://github.com/3b1b/manim)


## Install requirements

Manim depends on Python 2.7 and is not yet compatible with Python 3.

Manim dependencies rely on system libraries you will need to install on your
operating system:
* ffmpeg
* latex
* sox

Then you can install the python dependencies:
```sh
pip install -r requirements.txt
```

Note: pip will install the python module `aggdraw` from
https://github.com/scottopell/aggdraw-64bits/ and it might have additional
dependencies.

This doesn't install freetype, but I don't think it's required for this project

The latest version of aggdraw (1.3 as of 2018) does not work with manim. Uninstall it beforehand if necessary:
```sh
pip uninstall aggdraw
```

## How to Use
Try running the following:
```sh
python extract_scene.py example_scenes.py SquareToCircle -pl
```

The -p is for previewing, meaning the the video file will automatically open when it is done rendering.
Use -l for a faster rendering at a lower quality.
Use -s to skip to the end and just show the final frame.
Use -n (number) to skip ahead to the n'th animation of a scene.
Use -f to show the file in finder (for osx)

You will probably want to change the ANIMATIONS_DIR constant to be whatever directory you want video files to output to.

Look through the old_projects folder to see the code for previous 3b1b videos.  Note, however, that developments are often made to the library without considering backwards compatibility on those old_projects.  To run them with a guarantee that they will work, you will have to go back to the commit which complete that project.

While developing a scene, the `-s` flag is helpful to just see what things look like at the end without having to generate the full animation.  It can also be helpful to use the -n flag to skip over some number of animations.

Scene with `PiCreatures` are somewhat 3b1b specific, so the specific designs for various expressions are not part of the public repository.  You should still be able to run them, but they will fall back on using the "plain" expression for the creature.

## License

All files in the directories active_projects and old_projects, which by and large generate the visuals for 3b1b videos, are copyright 3Blue1Brown LLC.

The general purpose animation code found in the remainder of the repository, on the other hand, is under the MIT license.

## Docker Method
Since its a bit tricky to get all the dependencies set up just right, there is
a Dockerfile provided.

1. [Install Docker](https://www.docker.com/products/overview)
2. Build docker image. `docker build -t manim .`
3. Run it! `docker run --rm -v "$PWD/files":/app/files manim example_scenes.py WarpSquare`
