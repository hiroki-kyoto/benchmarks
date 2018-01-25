# Instructions for adding distributed benchmarks to continuous run:
(This version of benchmarks is a modified branch forked from a pretty early version which
yet suffers a serious network traffic  )

1. You can add your benchmark file under
   [tensorflow/benchmarks/scripts](https://github.com/tensorflow/benchmarks/tree/master/scripts) directory. The benchmark should accept `task_index`, `job_name`, `ps_hosts` and `worker_hosts` flags. You can copy-paste the following flag definitions:

    ```python
    tf.app.flags.DEFINE_integer("task_index", None, "Task index, should be >= 0.")
    tf.app.flags.DEFINE_string("job_name", None, "job name: worker or ps")
    tf.app.flags.DEFINE_string("ps_hosts", None, "Comma-separated list of hostname:port pairs")
    tf.app.flags.DEFINE_string("worker_hosts", None, "Comma-separated list of hostname:port pairs")
    ```
	for offload version, you're also expected to add/modify your offload_hosts in here:
	
	```python
	tf.app.flags.DEFINE_string("offload_hosts", None, "Comma-separated list of hostname:port pairs")
	```
	
2. modify the {job_name,task_index, device, data_format} respectively for each different 
	node(ps/worker/offload) , and Run tf_cnn_benchmarks.py on each node for test of version
	which does not contain offload roles; Run tf_cnn_benchmarks_offload.py on each node for
	test of offload version:
	
	```bash
	python tf_cnn_benchmarks.py
	python tf_cnn_benchmarks_offload.py
	```
	
For any questions, please contact annarev@google.com.
