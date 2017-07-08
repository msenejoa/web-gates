var chart = c3.generate({
    bindto: '#ten_strength',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_10.csv'
        },
    size:{
        height: 550
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#ten_quality',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_10_quality.csv'
        },
    size:{
        height: 270
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#thirteen_strength',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_13.csv'
        },
    size:{
        height: 550
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#thirteen_quality',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_13_quality.csv'
        },
    size:{
        height: 270
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#fourteen_strength',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_14.csv'
        },
    size:{
        height: 550
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#fourteen_quality',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_14_quality.csv'
        },
    size:{
        height: 270
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#fifteen_strength',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_15.csv'
        },
    size:{
        height: 550
        },
    axis: {
        x: {
            type: 'timeseries'}}
});

var chart = c3.generate({
    bindto: '#fifteen_quality',
    data: {
        x: 'Date',
        x_format: '%Y%m%d',
        url: '/static/mac_15_quality.csv'
        },
    size:{
        height: 270
        },
    axis: {
        x: {
            type: 'timeseries'}}
});
