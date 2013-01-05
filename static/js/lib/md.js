var MarkDown = function(){
	var self = {
		watch:function(){
			var $el = $(".area");
            $el.keyup(function(e){
                console.log($(".area").val());
                self.compileReq($(".area").val(),self.onCompileReq);
            });
		},
		render: function(data){
			return $(".output").html(data.text);
		},
		// convert to markdown syntax
		compileReq:function(text,callback){
			$.ajax({
				type: "POST",
				url: "/compile",
				dataType: "json",
				data: {"text": text},
				success:function(data){
					callback(data);
				}
			});
		},
        onCompileReq:function(data){
                         self.render(data);
        }
	};

	
	return self;
};





$(document).ready(function(){
	var md = MarkDown();
	md.watch();
	var init = function(){
		$(".area").val("");
	}();
	// init val

	console.log($("body"));
});



