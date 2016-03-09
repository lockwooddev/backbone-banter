"use strict";


define([
    'jquery',
    'underscore',
    'backbone',
    'collections/boards',
    'text!templates/welcomeTemplate.html',
    'views/ThreadListView',
], function($, _, Backbone, BoardCollection, welcomeTemplate, ThreadListView){

    var WelcomeView = Backbone.View.extend({
        el: $('#content'),

        events: {
            'click .welcome-nav': 'renderCatalog'
        },

        initialize: function(coll){
            this.coll = coll

            _.bindAll(this, 'render', 'renderCatalog');
        },

        render: function(){
            $(this.el).empty();

            var data = {
                boards: this.coll.models,
                _: _
            };

            var compiledTemplate = _.template(welcomeTemplate);
            this.$el.append(compiledTemplate(data));
        },

        renderCatalog: function(el){
            var targetArg = $(el.currentTarget).data('target');
            var threadListView = new ThreadListView(targetArg);
            threadListView.render();
        }
    });

    return WelcomeView;
});