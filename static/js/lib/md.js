var MarkDown = function(){
	var self = {
		watch:function(){
			var $el = $(".area");
			$el.keydown(function(e){
				self.compileReq($el.val(),self.onCompileReq);
			});
		},
		render: function(text){
			return $(".output").html(text);
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
			self.render(text);
		},
		onCompileReq:function(data){
		console.log(data.text);
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



