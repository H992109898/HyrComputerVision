function isLogin(){
	if($.cookie("username") == null){
		return false;
	}else{
		return true;
	}
}

function clickMyAccount(){
	if(isLogin()){
		window.location.href="myAccount.html";
	}else{
		window.location.href="login.html";
	}
}

function saveUserInfo() {
	var username = $("#username").val();
	var password = $("#password").val();
	
	$.cookie("rememberPassword", "true", { expires: 7 }); // 存储一个带7天期限的 cookie
	$.cookie("username", username, { expires: 7 }); // 存储一个带7天期限的 cookie
	$.cookie("password", password, { expires: 7 }); // 存储一个带7天期限的 cookie
	
}
		
function removeUserInfo(){
	$.cookie("rememberPassword", "false", { expires: -1 });
	$.cookie("username", '', { expires: -1 });
	$.cookie("password", '', { expires: -1 });
}