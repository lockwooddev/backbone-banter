"use strict";


define([
    'jquery',
    'underscore',
    'backbone',
    'collections/threads',
    'text!templates/threadListTemplate.html',
    'views/ThreadDetailView',
], function($, _, Backbone, ThreadCollection, threadListTemplate, ThreadDetailView){

    var ThreadListView = Backbone.View.extend({
        el: $('#content'),

        events: {
            'click .thread': 'renderThread'
        },

        initialize: function(options){
            this.options = options;
            _.bindAll(this, 'render', 'loadThreads', 'renderThread');

            this.collection = new ThreadCollection();
        },

        render: function(){
            console.log('render with options: '+ this.options);

            $(this.el).empty();
            this.collection.url = this.collection.url(this.options);

            $(".dropdown-toggle").html('Board: '+this.options+' <span class="caret"></span>')

            this.loadThreads();
        },

        loadThreads: function(){
            var that = this;

            this.collection.fetch({
                reset: true,
                success: function(collection, response, options) {
                    console.log('Success for '+ that.collection.url);

                    var data = {
                        threads: collection.models,
                        _: _,
                        board: that.options,
                    };

                    var compiledTemplate = _.template(threadListTemplate);
                    that.$el.append(compiledTemplate(data));
                },

                error: function(collection, response, options){
                    console.log('Error fetching '+ that.collection.url);
                }
            });
        },

        renderThread: function(el){
            var board = $(el.currentTarget).data('board');
            var id = $(el.currentTarget).data('no');

            console.log('Selected detail thread '+id+' on /'+board+'/');

            var threadDetailView = new ThreadDetailView(board, id);
            threadDetailView.render();
        }
    });

    return ThreadListView;
});