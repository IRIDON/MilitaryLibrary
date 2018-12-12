'use strict';
 
const gulp = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const csso = require('gulp-csso');
const debug = require('gulp-debug');
const rename = require("gulp-rename");
const gzip = require('gulp-gzip');
const gulpif = require('gulp-if');

const mainStylePath = '**/static/**/scss/';

global.DEV = false;
 
gulp.task('style', function () {
    return gulp.src(mainStylePath + 'main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: ['last 2 version', 'IE 10'],
            cascade: false,
            remove: false
        }))
        .pipe(csso())
        .pipe(rename(function (path) {
            path.dirname = path.dirname.replace('scss', 'css')
        }))
        .pipe(gulpif(!DEV, gzip()))
        .pipe(gulp.dest('./'));
});
 
gulp.task('watch', function () {
    global.DEV = false;

    gulp.watch(mainStylePath + '**/*.scss', ['style']);
});
