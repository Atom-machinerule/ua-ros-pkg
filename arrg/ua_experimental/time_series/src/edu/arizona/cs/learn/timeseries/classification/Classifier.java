package edu.arizona.cs.learn.timeseries.classification;

import java.util.List;
import java.util.Map;

import edu.arizona.cs.learn.algorithm.alignment.model.Instance;
import edu.arizona.cs.learn.timeseries.model.Episode;
import edu.arizona.cs.learn.util.SequenceType;

public abstract class Classifier {
	protected SequenceType _type;

	public Classifier(SequenceType type) {
		_type = type;
	}

	public abstract String getName();

	// return the amount of time it took to performing training
	// organized by class name.
	public abstract Map<String,Long> train(int fold, Map<String,List<Instance>> training);
	public abstract Map<String,Long> train(Map<String,List<Instance>> training);

	public abstract void trainEpisodes(int x, List<Episode> training, SequenceType type, boolean shuffle);
	public abstract void trainEpisodes(List<Episode> training, SequenceType type, boolean shuffle);

	public abstract String test(Instance testInstance);
}