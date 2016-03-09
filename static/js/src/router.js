"use strict";


define([
    'jquery',
    'underscore',
    'backbone',
    'views/index',
], function($, _, Backbone, IndexView){

    var AppRouter = Backbone.Router.extend({
        routes: {
            '/:id': 'showBoard'
        }
    });

    var initialize = function(){
        var appRouter = new AppRouter();

        var indexView = new IndexView();
        indexView.render();

        appRouter.on('showBoard', function(id){
            console.log('load board: ' + id);
        });

        Backbone.history.start();
    };

    return {
        initialize: initialize
    };
});