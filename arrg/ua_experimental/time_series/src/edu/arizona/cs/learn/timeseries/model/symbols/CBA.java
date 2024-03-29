package edu.arizona.cs.learn.timeseries.model.symbols;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.apache.log4j.Logger;
import org.dom4j.Element;

import edu.arizona.cs.learn.algorithm.bpp.BPPFactory;
import edu.arizona.cs.learn.timeseries.model.Interval;

public class CBA extends StringSymbol implements Comparable<CBA> {
	private static Logger logger = Logger.getLogger(CBA.class);

	private String _key;

	private int _start;
	private int _end;

	private List<Interval> _intervals;

	private List<String> _props;
	private List<Integer> _starts;
	private List<Integer> _ends;

	private boolean _finished = false;

	public CBA() {
		super(1.0);

		_start = Integer.MAX_VALUE;
		_end = 0;

		_intervals = new ArrayList<Interval>();

		_props = new ArrayList<String>();
		_starts = new ArrayList<Integer>();
		_ends = new ArrayList<Integer>();
	}
	
	public CBA(String key) {
		this(key, 1.0);
	}
	
	public CBA(String key, double weight) { 
		_key = key;
		_weight = weight;
	}

	public String toString() {
		return _key;
	}

	/**
	 * Add an interval to the list of intervals for this BPP.
	 * 
	 * @param interval
	 */
	public void addInterval(Interval interval) {
		if (_finished) {
			logger.error("Tried to add an interval to a CBA that is finished");
			return;
		}

		_intervals.add(interval);

		_props.add(interval.name);
		_starts.add(interval.start);
		_ends.add(interval.end);

		_start = Math.min(_start, interval.start);
		_end = Math.max(_end, interval.end);
	}
	
	public void finish() { 
		finish(true);
	}

	/**
	 * We are done adding intervals to this CBA so sort everything and retreive
	 * the key for this thing.
	 */
	public void finish(boolean makeKey) {
		if (makeKey) 
			_key = BPPFactory.bpp(_intervals, Interval.eff);

		Collections.sort(_starts);

		Collections.sort(_ends);
		Collections.reverse(_ends);

		_finished = true;
	}

	@Override
	public boolean equals(Object o) {
		if (!(o instanceof CBA))
			return false;

		CBA other = (CBA) o;
		return _key.equals(other._key);
	}

	@Override
	public int compareTo(CBA cba) {
		if (cba._intervals.size() != _intervals.size()) {
			throw new RuntimeException("Comparing CBA with different orders "
					+ _intervals.size() + " " + cba._intervals.size());
		}

		if (_end > cba._end)
			return 1;
		if (_end < cba._end)
			return -1;

		if (_start > cba._start)
			return 1;
		if (_start < cba._start)
			return -1;

		// compare all of the end points...
		for (int i = 0; i < _ends.size(); ++i) {
			int e1 = _ends.get(i);
			int e2 = cba._ends.get(i);

			if (e1 > e2)
				return 1;
			if (e1 < e2)
				return -1;
		}

		// compare all of the start points ...
		for (int i = 0; i < _starts.size(); ++i) {
			int s1 = _starts.get(i);
			int s2 = cba._starts.get(i);

			if (s1 > s2)
				return 1;
			if (s1 < s2)
				return -1;
		}

		// compare all of the propositions...
		for (int i = 0; i < _props.size(); ++i) {
			String n1 = _props.get(i);
			String n2 = cba._props.get(i);

			int comp = n1.compareTo(n2);
			if (comp > 0 || comp < 0) {
				return comp;
			}
		}

		// At this point everything is equal.... so what do we
		// do? Throw up our hands and throw an exception.
		throw new RuntimeException("Comparing the exact same CBAs - \n" + _key
				+ "\n" + cba._key);
	}

	@Override
	public List<Interval> getIntervals() {
		return _intervals;
	}

	@Override
	public String getKey() {
		return _key;
	}

	@Override
	public List<String> getProps() {
		return _props;
	}
	
	@Override
	public Symbol copy() { 
		throw new RuntimeException("Not yet implemented!");
	}
	
	@Override
	public Symbol merge(Symbol B) { 
		throw new RuntimeException("Not yet implemented!");
	}	

	public void toXML(Element e) {
		Element cba = e.addElement("symbol");
		
		cba.addAttribute("class", "CBA");
		cba.addAttribute("key", _key);
		cba.addAttribute("weight", _weight +"");

		for (Interval interval : _intervals)
			interval.toXML(cba);
	}

	public static CBA fromXML(Element e) {
		String key = e.attributeValue("key");
		double weight = Double.parseDouble(e.attributeValue("weight"));

		CBA cba = new CBA(key, weight);

		List list = e.elements("Interval");
		for (Object o : list) { 
			Interval i = Interval.fromXML((Element) o);
			cba.addInterval(i);
		}
		cba.finish(false);
		return cba;
	}

}
