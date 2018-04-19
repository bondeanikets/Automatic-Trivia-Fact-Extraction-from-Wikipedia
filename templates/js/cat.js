var index = 0;
var data = $('#my-data').data("name");
$(function() {
 for(var i = 0, size = 10; i < size ; i++){
   $('#catList').append('<li class="category">'+data[i]+'</li>');
 }
 index = 10;
});

$("#loadMore").click(function(){
  for(var i=index; i<index+5; i++){
   $('#catList').append('<li class="category">'+data[i]+'</li>');
 }
 index = index+5;
});