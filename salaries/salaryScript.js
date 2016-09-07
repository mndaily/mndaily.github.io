window.app = angular.module('salariesApp', ["ui.bootstrap", "ngResource"]);

app.controller('salariesControl', ["$scope", "$http", function($scope, $http) {
    $http.get("allSalaries.json").then(function(response) {
        $scope.myData = response.data.salaries;

	$scope.totalItems = $scope.myData.length;
	$scope.currentPage = 1;
	$scope.numPerPage = 10;
      
  $scope.paginate = function(value) {
    var begin, end, index;
    begin = ($scope.currentPage - 1) * $scope.numPerPage;
    end = begin + $scope.numPerPage;
    index = $scope.myData.indexOf(value);
    return (begin <= index && index < end);
  };});
}]);