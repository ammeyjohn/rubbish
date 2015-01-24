(function(R, $){

    /**
     * Functionility
     */
    R.el.is = function (type) { return this.type == (''+type).toLowerCase(); };
    R.el.o = function () { this.ox = this.x(); this.oy = this.y(); return this; };

    /**
     * Get the x, y coordinate of elememt
     */
    R.el.x = function(x) { return this.is('circle') ? this.attr('cx') : this.attr('x'); }
    R.el.y = function(y) { return this.is('circle') ? this.attr('cy') : this.attr('y'); }

    /**
     * Set the coordinate of element
     */
    R.el.setCoord = function(x, y) {

    }

    /**
     * Another one of my core extensions.
     * Raphael has getBBox(), I guess the "B" stands for Basic,
     * because I'd say the "A" in getABox() here stands for Advanced.
     */
    R.el.getABox = function () {

        var b = this.getBBox(); // thanks, I'll take it from here...

        var o = {
            // we'd still return what the original getBBox() provides us with
            x:              b.x,
            y:              b.y,
            width:          b.width,
            height:         b.height,

            // now we can actually pre-calculate the following into properties that are more readible for humans
            // x coordinates have three points: left edge, centered, and right edge
            xLeft:          b.x,
            xCenter:        b.x + b.width / 2,
            xRight:         b.x + b.width,


            // y coordinates have three points: top edge, middle, and bottom edge
            yTop:           b.y,
            yMiddle:        b.y + b.height / 2,
            yBottom:        b.y + b.height
        };


        // now we can produce a 3x3 combination of the above to derive 9 x,y coordinates

        // center
        o.center      = {x: o.xCenter,    y: o.yMiddle };

        // edges
        o.topLeft     = {x: o.xLeft,      y: o.yTop };
        o.topRight    = {x: o.xRight,     y: o.yTop };
        o.bottomLeft  = {x: o.xLeft,      y: o.yBottom };
        o.bottomRight = {x: o.xRight,     y: o.yBottom };

        // corners
        o.top         = {x: o.xCenter,    y: o.yTop };
        o.bottom      = {x: o.xCenter,    y: o.yBottom };
        o.left        = {x: o.xLeft,      y: o.yMiddle };
        o.right       = {x: o.xRight,     y: o.yMiddle };

        // shortcuts to get the offset of paper's canvas
        o.offset      = $(this.paper.canvas).parent().offset();

        return o;
    }


    /**
     * Routine drag-and-drop. Just el.draggable()
     * So instead of defining move, start, end and calling this.drag(move, start, end)
     */
    R.el.draggable = function (option) {

        // Extend the option with default value
        var opt = $.extend(true, { margin: 0 }, option || {});

        var onStart = function() {
            // store original pos, and bring the element to top
            this.o().toFront();
            
            // Make the element transparent when dragging.
            if(opt.opacity) {
                this.attr('opacity', opt.opacity);
            }
        },
        onMove = function(dx, dy, mx, my) {
            var b = this.getABox();
            var x = this.ox + dx;
            var y = this.oy + dy;

            var boundary = opt.boundary || {
                top:    b.offset.top,
                left:   b.offset.left,
                bottom: this.paper.height + b.offset.top,
                right:  this.paper.width + b.offset.left
            };

            var stroke_width = this.attr('stroke-width');
            var r = this.is('circle') ? b.width / 2 : 0;
            x = Math.max(x, boundary.left + r - stroke_width + opt.margin);
            y = Math.max(y, boundary.top + r - stroke_width + opt.margin);
            x = Math.min(x, boundary.right + r - b.width - stroke_width - stroke_width - opt.margin);
            y = Math.min(y, boundary.bottom + r - b.height - stroke_width - stroke_width - opt.margin);

            this.moveTo(x, y);
        },
        onEnd = function() {
            // Restore the opaque element
            this.attr('opacity', 1.0);
        }
        this.drag(onMove, onStart, onEnd);
    }

    /**
     * Move element to (x, y)
     */
    R.el.moveTo = function (x, y) {
        var coord = { };
        if(x) { coord.x = x; coord.cx = x; }
        if(y) { coord.y = y; coord.cy = y; }
        return this.attr(coord);
    }
    
})(Raphael, jQuery)
