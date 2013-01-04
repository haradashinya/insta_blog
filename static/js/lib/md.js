var MarkDown = function(){
	var self = {
		watch:function(){
			var $el = $(".area");
			$el.keydown(function(e){
				self.compile($el.val(),self.onCompile);
			});
		},
		render: function(text){
			return $(".output").html(text);
		},
		// convert to markdown syntax
		compile:function(text,callback){
			$.ajax({
				type: "POST",
				url: "/compile",
				dataType: "json",
				data: JSON.stringify({"text": text}),
				success:function(data){
					callback(data);
				}
			});
			self.render(text);
		},
		onCompile:function(data){
			console.log(data);
		}
	};



	
	return self;
};





$(document).ready(function(){
	var md = MarkDown();
	md.watch();
	console.log($("body"));
});



