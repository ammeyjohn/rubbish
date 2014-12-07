angular.module('wsdpDirectives', [])
    .directive('datepicker',
        function() { 

            var default_option = {
                format: 'yyyy-MM-dd',
                language: 'zh-CN',
                autoclose: true,
                calendarWeeks: false,
                clearBtn: true,
                startDate: '',
                endDate: '',
                forceParse: false,
                keyboardNavigation: true,
                minViewMode: 0,
                multidate: false,
                multidateSeparator: ',',
                orientation: 'auto',
                startView: 0,
                todayBtn: true,
                todayHighlight: true,
                weekStart: 0
            }

            return {
                restrict: 'AE',
                replace: true,
                transclude: true,
                scope: {
                    format: '@',
                    language: '@',
                    autoclose: '@',
                    calendarWeeks: '@',
                    clearBtn: '@',
                    startDate: '@',
                    endDate: '@',
                    forceParse: '@',
                    keyboardNavigation: '@',
                    minViewMode: '@',
                    multidate: '@',
                    orientation: '@',
                    startView: '@',
                    todayBtn: '@',
                    todayHighlight: '@',
                    weekStart: '@'
                },
                template: function(element, attrs) {
                    var type = attrs['type'];
                    if (!angular.isDefined(type) || type == null || type == '') {
                        type = 'input';
                    }

                    var template = '';
                    if (type == 'input') {
                        template = '<input type="text" class="form-control" />'; 
                    } else if (type == 'component') {
                        template = '<div class="input-group date">';
                        template += '   <input type="text" class="form-control">';
                        template += '   <span class="input-group-addon" ng-Transclude></span>';
                        template += '</div>';
                    } else if (type == 'inline') {
                        template = '<div></div>'
                    } else if (type == 'range') {

                        template = '<div class="input-daterange input-group" id="datepicker">';
                        template += '   <input type="text" class="input-sm form-control" name="start" />';
                        template += '   <span class="input-group-addon">to</span>';
                        template += '   <input type="text" class="input-sm form-control" name="end" />';
                        template += '</div>';

                    } else {
                        template = '<input type="text" />'; 
                    }
                    return template;
                },
                link: function(scope, element, attrs) {

                    var option = angular.extend({ }, default_option);

                    if (angular.isDefined(scope.language)) option.language = scope.language;
                    if (angular.isDefined(scope.format)) option.format = scope.format;
                    if (angular.isDefined(scope.autoclose)) option.autoclose = (scope.autoclose == 'true');
                    if (angular.isDefined(scope.calendarWeeks)) option.calendarWeeks= (scope.calendarWeeks== 'true');
                    if (angular.isDefined(scope.clearBtn)) option.clearBtn = (scope.clearBtn == 'true');
                    if (angular.isDefined(scope.forceParse)) option.forceParse = (scope.forceParse == 'true');
                    if (angular.isDefined(scope.keyboardNavigation)) option.keyboardNavigation= (scope.keyboardNavigation == 'true');
                    if (angular.isDefined(scope.minViewModel)) option.minViewMode = scope.minViewModel;
                    if (angular.isDefined(scope.multidate)) option.multidate = (scope.multidate == 'true');
                    if (angular.isDefined(scope.todayBtn)) option.todayBtn = (scope.todayBtn == 'true');
                    if (angular.isDefined(scope.todayHighlight)) option.todayHighlight = (scope.todayHighlight == 'true');

                    if (angular.isDefined(scope.startDate)) option.startDate = scope.startDate;
                    if (angular.isDefined(scope.endDate)) option.endDate = scope.endDate;
                    if (angular.isDefined(scope.orientation)) option.orientation = scope.orientation;
                    if (angular.isDefined(scope.startView)) option.startView = parseInt(scope.startView);
                    if (angular.isDefined(scope.weekStart)) option.weekStart = parseInt(scope.weekStart);

                    element.datepicker(option);
                }
            }; 
        });
