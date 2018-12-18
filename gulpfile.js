'use strict';
 
const gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    csso = require('gulp-csso'),
    debug = require('gulp-debug'),
    rename = require("gulp-rename"),
    gzip = require('gulp-gzip'),
    gulpif = require('gulp-if');

const path = require('path'),
    root = path.resolve(__dirname),
    mainPath = path.resolve(root , 'library', 'static', 'library'),
    mainStylePath = path.resolve(mainPath, 'scss');

global.DEV = false;

gulp.task('style', function () {
    return gulp.src(mainStylePath + '/main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: ['last 2 version', 'IE 10'],
            cascade: false,
            remove: false
        }))
        .pipe(csso())
        .pipe(debug())
        .pipe(gulpif(!DEV, gzip()))
        .pipe(gulp.dest(mainPath + '/css/'));
});
 
gulp.task('watch', function () {
    global.DEV = false;

    gulp.watch(mainStylePath + '/**/*.scss', ['style']);
});
