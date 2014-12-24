
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

                    if(value) {
                        if(typeof value !== define.type) {
                            value = attrParse(value, define.type);
                        }
                    } else {
                        value = define.value;
                    }
                    option[key] = value;

                    /* DEBUG */
                    console.log(key + ' = ' + value);
                });

                return option;
            }

            // Define the option properties
            var option_define = {
                autoclose: { type: 'boolean', value: true },
                language: { type: 'string', value: 'zh-CN' } 
            };

            return {
                restrict: 'AE',
                replace: true,
                transclude: true,
                scope: {
                    date: '=',
                    autoclose: '@',
                    language: '@'
                },
                template: function(element, attrs) {
                    var template = '';
                    template += '<div class="input-group date">';
                    template += '   <input type="text" class="form-control" ng-model="date">';
                    template += '   <span class="input-group-addon" ng-transclude></span>';
                    template += '</div>'; 
                    return template;
                },
                link: function(scope, element, attrs, ngModel) {
                    var option = optionAssign(option_define, scope);
                    element.datepicker(option);
                    element.datepicker('setDate', scope.date);
                }
            };
        });
