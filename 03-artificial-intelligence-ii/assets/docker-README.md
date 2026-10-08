Prerequisites: NVIDIA driver, Docker Engine, [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

From this directory:

```bash
docker compose up
```

Open the printed Jupyter URL, then verify GPU with `tf.config.list_physical_devices("GPU")`.

Adjust the image tag in `docker-compose.yml` when you standardize on a different TensorFlow release.
