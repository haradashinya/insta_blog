var MarkDown = function(){
    console.log("init");
    $(".area").empty();
	var self = {
		clear:function(){
			$(".area").empty();
		},
		watch:function(){
			var $el = $(".area");
            $el.keyup(function(e){
                console.log($(".area").val());
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


$('code').css({
    'overflow-x': 'scroll',
    'background-color': '#f6f6f6',
    'border': '1px dotted #ccc',
    'padding': '0.8em'
});
$('code').addClass('prettyprint');





