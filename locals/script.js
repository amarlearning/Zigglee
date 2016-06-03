var application = angular.module('myLanguage', []);
application.controller('language', function($scope) {
	$scope.myFavLanguage = 'None';

	$scope.php = function() {
		$scope.myFavLanguage = 'Php';		
	};

	$scope.javascript = function() {
		$scope.myFavLanguage = 'Javascript';		
	};

	$scope.cpp = function() {
		$scope.myFavLanguage = 'C++';		
	};

	$scope.python = function() {
		$scope.myFavLanguage = 'Python';		
	};

});