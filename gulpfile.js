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
    mainStylePath = '**/static/**/scss/';

global.DEV = false;
 
gulp.task('style', function () {
    return gulp.src(root + '/' + mainStylePath + 'main.scss')
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
