angular.module('directives', [])
    .directive('datepicker', 
        function() { 
            return {
                restrict: 'AE',
                replace: true,
                transclude: true,
                scope: {
                    value: '=ngModel'
                },
                template: function() {
                    var template = '';
                    template += '<div class="row">';
                    template += '   <div class="col-md-6" ng-transclude>';
                    template += '   </div>';
                    template += '</div>';
                    return template;
                },
                link: function(scope, element, attrs, ngModel) {
                    //var input = $element.find('input');
                    //$scope.$parent['ngform'].$addControl(input);
                },
                controller: function($scope, $element, $attrs, $transclude) {
                }
            };
        });
