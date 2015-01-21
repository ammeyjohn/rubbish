(function(R){

    /**
     * Another one of my core extensions.
     * Raphael has getBBox(), I guess the "B" stands for Basic,
     * because I'd say the "A" in getABox() here stands for Advanced.
     */
    var getABox = function () {

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
     * Get or set the coordinate x of element.
     */
    var x = function(x) {
        if(x && x != null) {
            if(this.is('circle')) {
                this.attr('cx', x);
            } else {
                this.attr('x', x);
            }
            return this;   
        } else {
            return this.is('circle') ? this.attr('cx') : this.attr('x');
        }
    }

    /**
     * Get or set the coordinate y of element.
     */
    var y = function(y) {
        if(y && y != null) {
            if(this.is('circle')) {
                this.attr('cy', y);
            } else {
                this.attr('y', t);
            }
            return this;   
        } else {
            return this.is('circle') ? this.attr('cy') : this.attr('y');
        }
    }

    /**
     * Routine drag-and-drop. Just el.draggable()
     * So instead of defining move, start, end and calling this.drag(move, start, end)
     */
    var draggable = function () {
        var onStart = function() {
            this.o().toFront();
        }
        var onMove = function(dx, dy) {
            moveTo(this, this.ox + dx, this.oy + dy);
        }

        var onEnd = function() {}
        this.drag(onMove, onStart, onEnd);
    }

    /**
     * Move element to (x, y)
     */
    var moveTo = function (el, x, y) {
        el.x(x).y(y);
    }
    
    /**
     * Export all functionility
     */
    R.el.is = function (type) { return this.type == (''+type).toLowerCase(); };
    R.el.o = function () { this.ox = this.x(); this.oy = this.y(); return this; };
    R.el.x = x;
    R.el.y = y;
    R.el.getABox = getABox;
    R.el.draggable = draggable;
})(Raphael)
