
angular.module('ngDirectives')
    .directive('ngDatepicker', 
        function() { 
            return {
                restrict: 'AE',
                replace: true,
                transclude: true,
                scope: {
                    date: '='
                },
                template: function(element, attrs) {
                    var template = '';
                    template += '<div class="input-group date">';
                    template += '   <input type="text" class="form-control" ng-model="date" required>';
                    template += '   <span class="input-group-addon" ng-transclude></span>';
                    template += '</div>'; 

                    var dom = $(template);

                    if(attrs['name']) {
                        dom.find('input').attr('name', attrs['name']);
                    }

                    if(attrs['required']) {
                        dom.find('input').attr('required', attrs['required']);
                    }


                    return dom[0].outerHTML;
                },
                link: function(scope, element, attrs, ngModel) {
                    
                    element.datepicker();
                    element.datepicker('setDate', scope.date);
                }
            };
        });
