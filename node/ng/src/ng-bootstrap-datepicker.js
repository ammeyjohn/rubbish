
angular.module('ngDirectives')
    .directive('ngDatepicker', 
        function() { 


            var attrParse = function(value, type) {

                if(!value || value === null) { return null; }
                if(!type) { return value; }

                switch(type) {
                    case 'string': return String(value);
                    case 'boolean': return value === 'true' || value === 1;
                    case 'number': return Number(value);
                }

                return value;
            }

            var optionAssign = function(defines, source) {

                if(!defines || defines === null) { return null; }
                if(!source || source === null) { return option; }

                // Create option instance
                var option = {}

                // According to the option definition, set all properties to option
                // If the type of value in source is not match the option
                // definition, the convertion will be applied.
                angular.forEach(defines, function(define, key) {
                    
                    var value = null;

                    var handle = source[key];
                    if(handle && angular.isFunction(handle)) {
                        // If the key in source is function object, the
                        // function should be excuted and the return value
                        // will be set to the value variable.
                        value = handle(key);
                    } else {
                        value = handle;
                    }

                    if(angular.isDefined(value)) {
                        if(typeof value !== define.type) {
                            value = attrParse(value, define.type);
                        }
                    } else {
                        value = define.value;
                    }

                    // If value is undefined, the property will not be
                    // set to the option.
                    if(angular.isDefined(value)) {
                        option[key] = value;

                        /* DEBUG */
                        if (value === '') { value = '""'; }
                        else if (typeof value === 'string') { 
                            value = '"' + value + '"'; 
                        }
                        console.log(key + ' = ' + value);
                    }
                });

                return option;
            }

            // To format the date object to string with format 'yyyy-MM-dd HH:mm:ss'
            var formatDate = function(date) {
                if(!date || date === null) return '';
                if(typeof date === 'string') {
                    return date;
                }

                return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate(); 
            }

            // To check whether the argument is type of date
            var isDate = function(date) {
                if(!date || date === null) return false;
                if(typeof date === 'string') {
                    var d = Date.parse(date);
                    return !isNaN(d);
                }
                return false;
            }

            // Define the option properties
            var option_define = {
                autoclose: { type: 'boolean', value: true },
                language: { type: 'string', value: 'zh-CN' },
                calendarWeeks: { type: 'boolean', value: false },
                clearBtn: { type: 'boolean', value: false },
                todayBtn: { type: 'boolean', value: false },
                daysOfWeekDisabled: { type: 'string' },
                startDate: { type: 'string' },
                endDate: { type: 'string' },
                forceParse: { type: 'boolean', value: true },
                format: { type: 'string', value: 'yyyy-mm-dd' },
                keyboardNavigation: { type: 'boolean', value: false },
                minViewMode: { type: 'string' },
                multidate: { type: 'boolean', value: false },
                multidateSeparator: { type: 'string' },
                orientation: { type: 'string' },
                startView: { type: 'string' },
                todayHighlight: { type: 'boolean', value: true },
                weekStart: { type: 'number' }
            };

            return {
                restrict: 'AE',
                replace: true,
                transclude: true,
                scope: {
                    date: '=',
                    autoclose: '@',
                    language: '@',
                    calendarWeeks: '@',
                    clearBtn: '@',
                    daysOfWeekDisabled: '@',
                    startDate: '=',
                    endDate: '=',
                    forceParse: '@',
                    format: '@',
                    keyboardNavigation: '@',
                    minViewMode: '@',
                    multidate: '@',
                    multidateSeparator: '@',
                    orientation: '@',
                    startView: '@',
                    todayBtn: '@',
                    todayHighlight: '@',
                    weekStart: '@'
                },
                template: function(element, attrs) {
                    var template = '';
                    template += '<div class="input-group date">';
                    template += '   <input type="text" class="form-control" ng-model="date">';
                    template += '   <span class="input-group-addon" ng-transclude></span>';
                    template += '</div>'; 
                    return template;
                },
                link: function(scope, element, attrs) {
                    // Initialize the component
                    var option = optionAssign(option_define, scope);
                    element.datepicker(option);
                    element.datepicker('setDate', scope.date);

                    // Attach event on the component
                    element.datepicker()
                        .on('changeDate', function(e) {
                            if(new Date(scope.date) - e.date !== 0) {
                                scope.date = formatDate(e.date);
                            }
                        });

                    // Create wather to monitor scope changed
                    scope.$watch('date', function(newValue, oldValue){
                        if(newValue !== oldValue) {
                            if(scope.date !== oldValue) {
                                if(isDate(newValue)) {
                                    element.datepicker('setDate', newValue);
                                }
                            }
                        } 
                    });
                }
            };
        });
