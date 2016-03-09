require.config({
    paths: {
        jquery: '../libs/jquery/jquery.min',
        underscore: '../libs/underscore/underscore.min',
        backbone: '../libs/backbone/backbone.min',
        bootstrap: '../libs/bootstrap/bootstrap.min',
    },

    shim: {
        jquery: {
            deps: [],
            exports: '$'
        },
        underscore: {
            deps: [],
            exports: '_'
        },
        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        bootstrap: {
            deps: ['jquery'],
            exports: '$'
        },
    }
});


require([
    // Load our app module and pass it to our definition function
    'app',
], function(App){
    // The "app" dependency is passed in as "App"
    App.initialize();
});
