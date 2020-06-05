const lookup = dict => key => is_null(dict) ?  undefined :
                              head(head(dict)) === key ? tail(head(dict)) :
                              lookup(tail(dict))(key);
const table = kvpairs => is_null(kvpairs) ? null :
              pair(pair(head(kvpairs), head(tail(kvpairs))), table(tail(tail(kvpairs))));

const flatten = xs => is_null(xs) ? null : !is_list(xs) ? list(xs) :
               append(is_list(head(xs)) ? flatten(head(xs)) : list(head(xs)),
                      flatten(tail(xs)));

const dispatch = list => lookup(table(list));
const map = f => list => is_null(list) ? null : pair(f(head(list)), map(f)(tail(list)));
const flatmap = f => list => flatten(map(f)(list));

const cons = tree => tree(cons);

const $ = x => is_string(x) ? x : (!is_function(x) || (x(".") === undefined)) ? stringify(x) : x(".");
const scan = x => (!is_function(x) || (x(scan) === undefined)) ? flatten(x) : x(scan);
const size = v => (!is_function(v) || (v(size) === undefined)) ? 1 : v(size);

const single = a => dispatch(list(
    cons, b => tree(digit1(b), empty, digit1(a)),
    scan, scan(a)
));    

const empty = dispatch(list(
    cons, single,
    scan, null
));

const tree = (left, subtree, right) => dispatch(list(
  cons, x => left(cons)(subtree, right)(x),
  scan, flatmap(scan)(list(right, subtree, left))
));

const digit1 = a => dispatch(list(
  cons, (subtree, right) => x => tree(digit2(x,a), subtree, right),
  scan, flatmap(scan)(list(a))
));

const digit2 = (a,b) => dispatch(list(
  cons, (subtree, right) => x => tree(digit3(x,a,b), subtree, right),
  scan, flatmap(scan)(list(b,a))
));

const digit3 = (a,b,c) => dispatch(list(
  cons,(subtree, right) => x => tree(digit4(x,a,b,c), subtree, right),
  scan, flatmap(scan)(list(c,b,a))
));

const digit4 = (a,b,c,d) => dispatch(list(
  cons,(subtree, right) => x => tree(digit2(x,a),subtree(cons)(node3(b,c,d)),right),
  scan, flatmap(scan)(list(d,c,b,a))
));

const node2 = (a,b) => dispatch(list(
  scan, flatmap(scan)(list(b,a))
));

const node3 = (a,b,c) => dispatch(list(
  scan, flatmap(scan)(list(c,b,a))
));

const build = n => n === 0 ? empty : build(n-1)(cons)(n);
const t = build(30);
scan(t);