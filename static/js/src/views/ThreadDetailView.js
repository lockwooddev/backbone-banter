"use strict";


define([
    'jquery',
    'underscore',
    'backbone',
    'collections/posts',
    'text!templates/threadDetailTemplate.html',
], function($, _, Backbone, PostCollection, threadDetailTemplate){

    var ThreadDetailView = Backbone.View.extend({
        el: $('#content'),

        initialize: function(board, thread_id){
            this.board = board;
            this.thread_id = thread_id;
            _.bindAll(this, 'render', 'loadPosts');

            this.collection = new PostCollection();
            this.collection.url = this.collection.url(this.board, this.thread_id);
        },

        render: function(){
            $(this.el).empty();
            this.loadPosts();
        },

        loadPosts: function(){
            var that = this;

            this.collection.fetch({
                success: function(collection, response, options) {
                    console.log('Success for '+ that.collection.url);

                    var data = {
                        posts: collection.models,
                        _: _,
                        board: that.board,
                    };

                    var compiledTemplate = _.template(threadDetailTemplate);
                    that.$el.append(compiledTemplate(data));
                },

                error: function(collection, response, options){
                    console.log('Error fetching '+ that.collection.url);
                }
            });
        }
    });

    return ThreadDetailView;
});