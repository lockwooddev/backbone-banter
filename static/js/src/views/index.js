"use strict";


define([
    'jquery',
    'underscore',
    'backbone',
    'collections/boards',
    'views/NavigationView',
    'views/WelcomeView',
], function($, _, Backbone, BoardCollection, NavigationView, WelcomeView){

    var IndexView = Backbone.View.extend({

        initialize: function(){
            _.bindAll(this, 'render');

            this.collection = new BoardCollection();
        },

        render: function(){
            this.loadBoards();
        },

        loadBoards: function(){
            var that = this;

            this.collection.fetch({
                success: function(collection, response, options) {
                    // use collection.url ?
                    console.log('Success for '+ that.collection.url);

                    console.log(collection.models)

                    var navigationView = new NavigationView(collection);
                    navigationView.render();

                    var welcomeView = new WelcomeView(collection);
                    welcomeView.render();
                },

                error: function(collection, response, options){
                    console.log('Error fetching '+ that.collection.url);
                }
            });
        }
    });

    return IndexView;
});