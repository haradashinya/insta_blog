var MarkDown = function(){
	$(".area").html($(".area").val().trim());
	var self = {
		clear:function(){
			$(".area").empty();
		},
		watch:function(){
			var $el = $(".area");
            $el.keyup(function(e){
                if (e.keyCode === 13){
                }
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


var md = MarkDown();
md.watch();







