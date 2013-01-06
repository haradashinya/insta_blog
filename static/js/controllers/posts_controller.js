window.PostsController = function(){
	$(".edit").bind("click",function(){
		console.log("called");
	});
    var that = {
        compileReq:function(text,callback){
                       $.ajax({
                           type: "POST",
                           url: "/show_compile",
                           dataType: "json",
                           data: {"text": "foooo"},
                           success:function(data){
                             callback(data);
                            }
                       });
                   },
        onCompileReq:function(data){
                         console.log(data);
                         console.log("init");
                     }
    };



    return that;
};

var postsController = PostsController();
postsController.compileReq("text",postsController.onCompileReq);


